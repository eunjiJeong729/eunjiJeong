def __create_LineString(self, df):
    """apply 활용 함수 geometry data 3차원 연산"""
    xy = np.array(df.geometry.coords)
    z = np.array(df.height)
    z = np.vstack([z] * len(xy))
    xyz = np.hstack((xy, z))
    df_geo = LineString(xyz).wkt
    return df_geo

def __process(self, pro_df):
    """데이터 프레임 전처리(geometry3d 연산)"""
    pro_df['geometry3d'] = pro_df.apply(self.__create_LineString, axis=1)
    pro_df['geometry'] = pro_df['geometry'].apply(lambda x: x.wkt)