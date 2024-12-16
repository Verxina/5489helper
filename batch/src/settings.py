from pydantic_settings import BaseSettings, SettingsConfigDict

# 設定モデルを定義
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
    
    inputDepartStName: str
    inputArriveStName: str 
    inputDate: str
    inputHour: str
    inputMinute: str
    inputType: str
    inputUniqueDepartSt: str
    inputUniqueArriveSt: str
    inputSearchType: str
    inputSpecificBriefTrainKana1: str
    inputTransferDepartStName1: str
    inputTransferArriveStName1: str
    inputTransferDepartStUnique1: str
    inputTransferArriveStUnique1: str
    inputTransferTrainType1: str
    inputSpecificTrainType1: str

    name1: str
    name2: str
    tel1: str
    tel2: str
    tel3: str
    email: str

    wait_10_o_clock: bool
