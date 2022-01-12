import easygui as eg
import data_writer
import predictor
import decimal

def half_up(x):
    decimal.getcontext().prec = 4
    ix = decimal.Decimal(int(x))
    ix2 = decimal.Decimal(ix+1)
    x = decimal.Decimal(x)
    dx_up = abs(ix2-x)
    dx_down = abs(ix-x)
    if dx_up <= dx_down:
        r = ix2
    else:
        r = ix
    return int(r)

def main():
    m_b = eg.boolbox
    m_e = eg.enterbox
    times = int(m_e("How many pairs of data do you want to generate?"))
    detail__ = m_b("Do you want to show more details?", choices=("[Y]es", "[N]o"))
    real_result = data_writer.main(times, detail__)
    result_after_training = predictor.main(detail__)
    bool_return = real_result == half_up(result_after_training)
    print(real_result, half_up(result_after_training))
    if bool_return:
        print("TRUE.")
    else:
        print("FALSE.")
    return bool_return

if __name__=="__main__":
    main()