from datasets import load_dataset

if __name__ == '__main__':
    infile_path = '/home/jschmolzi/anserini/collections/msmarco-doc-json-base/docs00aa.json'
    dataset = load_dataset('json', data_files=infile_path, split='train[:100]')
    print(dataset)
    
    new_column = [False] * len(dataset)
    dataset = dataset.add_column("is_prefix", new_column)
    print(dataset)
    
    print(dataset['is_prefix'])
    counter = 0
    
    for value in dataset['is_prefix']:
        print("Line %d: %s" % (counter, value))
        counter = counter + 1