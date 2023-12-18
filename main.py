from functions import get_predictions


if __name__ == '__main__':
    file_path = 'data/sample.csv'

    predictions = get_predictions(file_path=file_path)

    print(predictions)
