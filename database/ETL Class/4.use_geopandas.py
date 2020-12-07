def get_df(file_path):
    '''파일 위치에서 data load'''
    df = gpd.read_file(f"{file_path}", encoding="cp949")
    result = df.rename(columns={'A': 'B'})
    resul2 = df.rename(columns={'A': 'C'})
    merge_df = gpd.GeoDataFrame(pd.concat([result, resul2], ignore_index=True))
    return merge_df

def __retrieve_df(self, table_name, need_cd, need_type):
    '''sqlalchemy connect.py에 있는 __get_data_from_table 활용
        기존 테이블 사용 시'''
    query = f'''
        SELECT 
            *
        FROM {table_name} 
        WHERE 1 = 1
            AND
            A like '{need_cd}%'
            AND 
            type = '{need_type}' '''
    need_df = self.__get_data_from_table("db_name", query)
    return need_df.set_index("need_type").to_dict().get("region_cd")