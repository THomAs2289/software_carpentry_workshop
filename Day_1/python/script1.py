import pandas,sys
input_file=sys.argv[1]
col=sys.argv[2]
df=pandas.read_csv(input_file, sep='\t')
import matplotlib.pyplot as plt
plt.hist(df[col])
plt.savefig('Poor_people.jpg')
plt.show()
