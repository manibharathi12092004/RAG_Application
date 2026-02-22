import re

# NEW Langchain splitter package
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Import extraction file
from extract_policies import read_all_policies


# =====================================================
# SPLIT INTO BILLING / REFUND / CANCELLATION
# =====================================================

def split_sections(text):

    sections = {}

    patterns = {

        "billing":
        r"(SECTION\s*1.*?)(?=SECTION\s*2|$)",

        "refund":
        r"(SECTION\s*2.*?)(?=SECTION\s*3|$)",

        "cancellation":
        r"(SECTION\s*3.*)"
    }

    for name, pattern in patterns.items():

        match = re.search(

            pattern,
            text,
            re.IGNORECASE | re.DOTALL

        )

        if match:

            sections[name] = match.group(1)

    return sections


# =====================================================
# SMART CHUNKING
# =====================================================

def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,
        chunk_overlap=200,

        separators=[

            "\n\n",
            "\n",
            ". ",
            " "
        ]
    )

    return splitter.split_text(text)


# =====================================================
# CREATE DOCUMENTS + METADATA
# =====================================================

def create_documents(policy_texts):

    documents = []

    for filename, full_text in policy_texts.items():

        provider = filename.replace(
            ".pdf", ""
        ).lower()

        print(f"\nProcessing -> {provider}")

        # split billing/refund/cancel
        sections = split_sections(full_text)

        for policy_type, section_text in sections.items():

            chunks = chunk_text(section_text)

            print(
                f"{provider} | {policy_type} -> {len(chunks)} chunks"
            )

            # RESET counter for each section
            chunk_counter = 0

            for chunk in chunks:

                documents.append({

                    "text": chunk,

                    "provider": provider,

                    "policy_type": policy_type,

                    "source_file": filename,

                    "chunk_id": chunk_counter

                })

                chunk_counter += 1

    return documents


# =====================================================
# MAIN EXECUTION
# =====================================================

if __name__ == "__main__":

    print("\n========== STEP 7 PDF EXTRACTION ==========\n")

    policies = read_all_policies()

    print("\n========== STEP 8 SMART CHUNKING ==========\n")

    documents = create_documents(policies)

    print("\nChunking Completed")

    print(
        f"\nTotal Documents Created -> {len(documents)}"
    )


    # ==========================================
    # PRINT SAMPLE METADATA
    # ==========================================

    if documents:

        sample = documents[0]

        print("\n========== SAMPLE METADATA ==========\n")

        print("Provider :", sample["provider"])

        print("Policy Type :", sample["policy_type"])

        print("Source File :", sample["source_file"])

        print("Chunk ID :", sample["chunk_id"])

        print("\nText Preview:\n")

        print(sample["text"][:400])