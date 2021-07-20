from icecream import ic
import pandas as pd


def run():
    """
    Importante revisar que al momento de trabajar con dataframes, el orden de
    los datos varia si se declara por medio de diccionario contra la
    declaración por medio de lista de listas. El indexado de los datos
    cambia
    
    """
    series_test = pd.Series([100, 200, 300])
    ic(series_test)

    series_test2 = pd.Series({
        1999: 48000,
        2000: 65000,
        2001: 89000})
    ic(series_test2)

    frame_test = pd.DataFrame({
        1999: [78, 21, 54],
        2000: [54, 82, 20],
        2001: [1, 5 ,4]})
    ic(frame_test)

    frame_test2 = pd.DataFrame([
        [78, 21, 54],
        [54, 82, 20],
        [1, 5 ,4]])
    ic(frame_test2)

    frame_test2 = pd.DataFrame([
        [78, 21, 54],
        [54, 82, 20],
        [1, 5 ,4]], columns = [1999, 2000, 2001])
    ic(frame_test2)


if __name__ == '__main__':
    run()