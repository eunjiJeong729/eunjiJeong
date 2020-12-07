class ETL:
    """ETL"""
    def __init__(self, file_path, db_name, csv_save_path):
        self.path = file_path
        self.db_name = db_name
        self.csv_save_path = csv_save_path

    def run(self):
        data = self.__get_df()
        df = self.__process(data)
        self.__save(df)
        self.__save_file(df)

if __name__ == "__main__":
    ETL('file_path', 'db_name', 'csv_save_path').run()