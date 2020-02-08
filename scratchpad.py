alpha = [2,8,1]
bravo = [7,0,2]
charlie = [1,1,5,6]

samples = [alpha,bravo,charlie]
def get_mean(sample):
    sample_sum = sum(sample)
    sample_len = len(sample)
    return sample_sum/sample_len

foo = [map(get_mean,samples) for sample in samples]
print(foo)