from Bio import SeqIO

def extract_ids_from_hmmsearch(file_name):
    protein_ids = set()
    inclusion_threshold_reached = False
    
    with open(file_name, 'r') as file:
        for line in file:
            if "Domain annotation for each sequence (and alignments):" in line:
                inclusion_threshold_reached = True
            if inclusion_threshold_reached:
                break
            parts = line.split()
            if parts and parts[0][0].isdigit():
                protein_ids.add(parts[8].split(".")[0])
                
    return protein_ids

def filter_fasta_by_ids(input_fasta, output_fasta, ids):
    with open(input_fasta, 'r') as fasta, open(output_fasta, 'w') as output:
        for record in SeqIO.parse(fasta, "fasta"):
            # Check if protein ID is in the set of extracted IDs
            if record.id.split(".")[0] not in ids:
                SeqIO.write(record, output, "fasta")

if __name__ == "__main__":
    root_path = "C:/Users/Leo/Desktop/MRes/Litreview/FullProteome/FullProteome"
    for dirs in [{"dir_seq":"SolanumLycopersicumNCBI", "text_file":"kinase_matches.txt"},
                 {"dir_seq":"SolanumLycopersicum_Heinz_UniProt_1706", "text_file":"kinase_matches.txt"},
                 {"dir_seq":"SolanumLycopersicum_Alisa_Craig_InterPro_UP000004994", "text_file":"kinase_matches.txt"}]:
        
        hmmsearch_file = f"{root_path}/{dirs['dir_seq']}/{dirs['text_file']}"
        input_fasta_file = f"{root_path}/{dirs['dir_seq']}/sequence_filtered.fasta"
        output_fasta_file = f"{root_path}/{dirs['dir_seq']}/sequence_filtered_non_kinase.fasta"
        
        protein_ids = extract_ids_from_hmmsearch(hmmsearch_file)
        filter_fasta_by_ids(input_fasta_file, output_fasta_file, protein_ids)