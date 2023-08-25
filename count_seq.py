#"sequence > sequence_fil > sequence_fil_Non_Ki > signal > signal_fil"

def count_sequences(fasta_file):
    sequence_count = 0

    with open(fasta_file, 'r') as file:
        for line in file:
            if line.startswith('>'):
                sequence_count += 1

    return sequence_count

root_path = 'C:/Users/Leo/Desktop/MRes/Litreview/FullProteome/FullProteome'
dirs = ['SolanumLycopersicumNCBI','SolanumLycopersicum_Heinz_UniProt_1706','SolanumLycopersicum_Alisa_Craig_InterPro_UP000004994']
fasta_file_paths = ['sequence','sequence_filtered','sequence_filtered_non_kinase','signal','signal_filtered']

for Dir in dirs:
    print(Dir)
    for fasta in fasta_file_paths:
        num_sequences = count_sequences(f'{root_path}/{Dir}/{fasta}.fasta')
        print(f"\tNumber of sequences in {fasta}:", num_sequences)