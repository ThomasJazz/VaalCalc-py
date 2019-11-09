import csv
class MethodHelper:
    def __init__(self):
        pass

    # Write 2dlist to csv file
    def export_list_to_csv(self, file_path, dataset):
        with open(file_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(dataset)
        return