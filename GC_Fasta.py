x = open(input(""))
x_read =x.read()
new =""
for line in x_read:
    if line.startswith(">"):
        yo= x_read.split("\n")
fasta_label=""
fasta_dict = {}
for line in yo:
    if ">" in line:
        fasta_label = line
        fasta_dict[fasta_label]= ""
    else:
         fasta_dict[fasta_label] += line

def gc(sequence):
    G = sequence.count("G")
    C = sequence.count("C")
    Total = len(sequence)
    GC_Content = ((G+C)/Total)* 100
    return round (GC_Content, 6)

result ={key:gc(value) for (key,value) in fasta_dict.items()}

maximum = max(result, key=result.get)
yoh = maximum.replace(">","")
print(f"{yoh}\n{result[maximum]}")