def parse_gff(gff_file_path):
    protein_ids = set()
    with open(gff_file_path, 'r') as f:
        for line in f:
            if "Number of predicted TMRs:" in line and not "Number of predicted TMRs: 0" in line:
                protein_id = line.split()[1]
                protein_ids.add(protein_id)
    return protein_ids

def filter_fasta(fasta_file_path, protein_ids, output_file_path):
    with open(fasta_file_path, 'r') as f, open(output_file_path, 'w') as out:
        write_seq = False
        for line in f:
            if line.startswith('>'):
                protein_id = line[1:].split()[0]
                write_seq = protein_id in protein_ids
            if write_seq:
                out.write(line)

def main(gff_file_path, fasta_file_path, output_file_path):
    protein_ids = parse_gff(gff_file_path)
    filter_fasta(fasta_file_path, protein_ids, output_file_path)

if __name__ == "__main__":
    #import sys
    #if len(sys.argv) != 4:
    #    print("Usage: script_name.py <path_to_gff> <path_to_fasta> <path_to_output_fasta>")
    #    sys.exit(1)

    root_dir = "C:/Users/Leo/Desktop/MRes/Litreview/FullProteome/FullProteome"
    dtu_dir = "DTU_DeepTMHMM_1.0.24-results"
    for dirs in ["SolanumLycopersicumNCBI", 
                "SolanumLycopersicum_Heinz_UniProt_1706", 
                "SolanumLycopersicum_Alisa_Craig_InterPro_UP000004994"]:
        gff_file_path = f"{root_dir}/{dirs}/{dtu_dir}/TMRs.gff3"
        fasta_file_path = f"{root_dir}/{dirs}/signal.fasta"
        output_file_path = f"{root_dir}/{dirs}/signal_filtered.fasta"
        main(gff_file_path, fasta_file_path, output_file_path)