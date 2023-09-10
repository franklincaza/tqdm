from tqdm.auto import tqdm
for i in tqdm(range(100000000)):
	print(" ",end='\r')


for i, x in enumerate(list(range(10000))):
	print(i,end='\r')


from tqdm import tqdm
loop = tqdm(total = 5000, position=0, leave=False)
for i in tqdm(range(5000)):
	loop.set_description("LOADING...".format(i))
	loop.update(1)
loop.close()
