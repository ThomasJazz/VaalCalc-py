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


    # Writes an excel file to 'file_path' with values in 2d list named 'data'
    def export_2dlist_to_xlsx(self, file_path: str, data: list):
        try: 
            book = xlsxwriter.Workbook(file_path)                       # Make new workbook
            sheet = book.add_worksheet("Report")
            
            date_format = book.add_format({'num_format': 'm/d/yyyy'})   # Format dates

            for row in range(0, len(data)):
                for col in range(0, len(data[row])):
                    report_item = data[row][col]

                    if not(report_item is None):
                        if (isinstance(report_item, datetime)):
                            sheet.write(row, col, report_item, date_format)
                        else:                               # Generic format
                            sheet.write(row, col, report_item)
                    else:
                        sheet.write(row, col, '')
    
        except Exception as e:
            self.add_message("Failed while writing to file: " + file_path, 1)
            self.add_message("Exception: " + str(e), 1)
        finally:
            book.close()