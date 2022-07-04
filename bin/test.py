from datasets import load_dataset

if __name__ == '__main__':
    infile_path = '/home/jschmolzi/anserini/collections/msmarco-doc-json-base/docs00aa.json'
    dataset = load_dataset('json', data_files=infile_path, split='train[10:20]')    
    dataset.select(range(100))
    dataset = dataset['train']
    print(dataset)