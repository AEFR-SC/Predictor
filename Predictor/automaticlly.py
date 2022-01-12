import easygui as eg
import data_writer
import predictor


def main():
    m_b = eg.boolbox
    m_e = eg.enterbox
    times = int(m_e("How many pairs of data do you want to generate?"))
    detail__ = m_b("Do you want to show more details?", choices=("[Y]es", "[N]o"))
    real_result = data_writer.main(times, detail__)
    result_after_training = predictor.main(detail__)
    bool_return = abs(real_result-result_after_training)<=1
    if bool_return:
        print("TRUE.")
    else:
        print("FALSE.")
    return bool_return

if __name__=="__main__":
    main()