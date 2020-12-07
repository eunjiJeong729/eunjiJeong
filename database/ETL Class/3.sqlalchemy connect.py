def __get_data_from_table(self, dbname, query_txt):
    '''DB에서 get'''
    connect_str = f'host={host} user={user} password = {pw}' + f" dbname = {dbname}"
    with pg.connect(connect_str) as conn:
        df = pd.read_sql_query(query_txt, con=conn)
    return df

def __save(self, df):
    '''DB에 save'''
    dbname = self.db_name
    table_name = 'need_table'
    engine_string = f'postgresql+psycopg2://{user}:{pw}@{host}' + f'{dbname}'
    '''executemany_mode로 속도 개선'''
    engine = create_engine(engine_string, executemany_mode="batch")

    df.to_sql(f'{table_name}', con=engine, if_exists='append', index=False, method='multi', chunksize=10000)

def __save_file(self, df):
    '''csv 파일로 save'''
    df.to_csv(f'{self.csv_save_path}/ETL.csv', mode='w')