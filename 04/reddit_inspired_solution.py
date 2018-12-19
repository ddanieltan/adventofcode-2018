#%%
import collections

guards = collections.defaultdict(list)
times= collections.defaultdict(int)

#%%
for line in sorted(open('input.txt')):
