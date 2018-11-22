s1 = ' bottles of beer on the wall'
s2 = ' bottles of beer.'
s3 = 'Take one down and pass it around, '
for i in range(99,2,-1):
	print(f"{i}{s1}, {i}{s2}\n{s3}{i-1}{s1}.\n\n")
print(f"{2}{s1}, {2}{s2}\n{s3}{1}{s1[:7]+s1[8:]}.\n\n")
print(f"{1}{s1[:7]+s1[8:]}, {1}{s2[:7]+s2[8:]}\n{s3}{'no more'}{s1}.\n\n")
print(f"{'No more'}{s1}, {'no more'}{s2}\n{'Go to the store and buy some more, '}{99}{s1}.\n\n")