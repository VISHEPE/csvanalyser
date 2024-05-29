import pandas as pd

def load_csv(file_path):
    data = pd.read_csv(file_path)
    return data

def analyze_data(data):
    print("Data Shape:", data.shape)
    print("Data Columns:", data.columns)
    print("Data Head:", data.head())
    print("Data Info:", data.info())
    print("Data Describe:", data.describe())

def write_to_csv(data, file_path):
    data.to_csv(file_path, index=False)

def main():
    file_path = 'data.csv'
    data = load_csv(file_path)
    analyze_data(data)
    write_to_csv(data, 'output.csv')

if __name__ == '__main__':
    main()