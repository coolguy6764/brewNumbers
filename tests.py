from formulas import *

og_fg_cases = [[1.155, 0.099], # Extremes
               [1.065, 1.014], # Normal Range
               [1.014, 1.012], # Abnormal Low OG, Lower FG
               [1.0, 0.095],   # Abnromal Unrealisticaly Low OG and FG
               [1.155, 1.100]] # Abnromal Unrealistically High OG and FG

              ## Add test cases for Normal Range High Gravity Beer

def test_real_gravity():
    # TODO - return error if original_gravity < final_gravity
    answers = [-432.1081205938837,
              5.921449312563847,
              3.1587652264371897,
              -455.64019167531416,
              26.08821154572511]
    for case in range(len(og_fg_cases)):
        assert real_extract(og_fg_cases[case][0], og_fg_cases[case][1]) == answers[case]


def test_alcohol_content():
    # TODO - return error if original_gravity < final_gravity
    answers = [276.485653378602,
              5.251046681435098,
              0.20354144069428465,
              220.48559821800364,
              5.428436818971364]
    for case in range(len(og_fg_cases)):
        assert alcohol_content(og_fg_cases[case][0], og_fg_cases[case][1]) == answers[case]


def test_calories():
    # TODO - return error if original_gravity < final_gravity
    answers = [70.30652059785925,
               221.17256809702883,
               51.49239936304469,
               -99.00453814834444, # TODO: Explore why this is the case
               566.1539466555014]
    for case in range(len(og_fg_cases)):
        assert calories(og_fg_cases[case][0], og_fg_cases[case][1]) == answers[case]


def test_corr_fact():
    temps_answers = [[32, 0.9990055598467992],
                     [60, 1.0000631327683198],
                     [85, 1.0031650678740949],
                     [100, 1.00590829772],
                     [150, 1.0191492685049999],
                     [199, 1.0369529405660813],
                     [200,  1.0373543977599997]]
    for temp_answer in temps_answers:
        assert correction_factor(temp_answer[0]) == temp_answer[1]


def test_corr_sg():
    gravities_temps_answers = [[0.95, 32, 0.9490055598467991],
                               [0.95, 65, 0.9505283595925549],
                               [0.95, 120, 0.9604972329625598],
                               [0.95, 200, 0.9873543977599997],
                               [1.065, 32, 1.064005559846799],
                               [1.065, 65, 1.0655283595925549],
                               [1.065, 120, 1.0754972329625598],
                               [1.065, 200, 1.1023543977599997],
                               [1.999, 32, 1.9980055598467992],
                               [1.999, 65, 1.999528359592555],
                               [1.999, 120, 2.00949723296256],
                               [1.999, 200, 2.03635439776],
                               ]
    for g_t_a in gravities_temps_answers:
        assert corrected_sg(g_t_a[0], g_t_a[1]) == g_t_a[2]


def test_extract():
    gravities_answers = [[0.99, -2.609043939999765],
                         [.99, -2.609043939999765],
                         [1.014, 3.571630427359935],
                         [1.065, 15.883237647500295],
                         [1.099, 23.52729088906014],
                         [1.111, 26.127321605140025],
                         [1.999, 213.3863110270604]]
    for g_a in gravities_answers:
        assert extract(g_a[0]) == g_a[1]


def test_how_much_sugar():
    inputs_answers = [[33, 33, 1, 475.98431784975],
                     [60, 33, 1, 486.3910383],
                     [80, 33, 1, 490.3067898],
                     [33, 10, 1, 126.49931784975],
                     [60, 10, 1, 136.9060383],
                     [80, 10, 1, 140.8217898],
                     [33, 60, 1, 886.24931784975],
                     [60, 60, 1, 896.6560383000001],
                     [80, 60, 1, 900.5717898000001],
                     [33, 33, 5, 2379.9215892487496],
                     [60, 33, 5, 2431.9551914999997],
                     [80, 33, 5, 2451.5339489999997],
                     [33, 10, 5, 632.49658924875],
                     [60, 10, 5, 684.5301915],
                     [80, 10, 5, 704.1089489999999],
                     [33, 60, 5, 4431.24658924875],
                     [60, 60, 5, 4483.2801915],
                     [80, 60, 5, 4502.858949],
                     [33, 33, 10, 4759.843178497499],
                     [60, 33, 10, 4863.9103829999995],
                     [80, 33, 10, 4903.067897999999],
                     [33, 10, 10, 1264.9931784975],
                     [60, 10, 10, 1369.060383],
                     [80, 10, 10, 1408.2178979999999],
                     [33, 60, 10, 8862.4931784975],
                     [60, 60, 10, 8966.560383],
                     [80, 60, 10, 9005.717898],
                     [33, 33, 15, 7139.76476774625],
                     [60, 33, 15, 7295.865574500001],
                     [80, 33, 15, 7354.601847000001],
                     [33, 10, 15, 1897.48976774625],
                     [60, 10, 15, 2053.5905745],
                     [80, 10, 15, 2112.3268470000003],
                     [33, 60, 15, 13293.73976774625],
                     [60, 60, 15, 13449.840574500002],
                     [80, 60, 15, 13508.576847000002],
                     [33, 33, 55, 26179.137481736252],
                     [60, 33, 55, 26751.5071065],
                     [80, 33, 55, 26966.873439],
                     [33, 10, 55, 6957.46248173625],
                     [60, 10, 55, 7529.8321065],
                     [80, 10, 55, 7745.198439000001],
                     [33, 60, 55, 48743.71248173625],
                     [60, 60, 55, 49316.082106500005],
                     [80, 60, 55, 49531.44843900001]]
    for case in inputs_answers:
        assert how_much_sugar(case[0],case[1],case[2]) == case[3]


def test_carbon_dioxide():
    inputs_answers =    [[33,5,1,2.0039929499999998],
                        [60,5,1,1.3191149999999998],
                        [80,5,1,1.0614149999999993],
                        [33,200,1,14.837137949999999],
                        [60,200,1,14.152259999999998],
                        [80,200,1,13.894559999999998],
                        [33,2000,1,133.29693794999997],
                        [60,2000,1,132.61205999999999],
                        [80,2000,1,132.35435999999999],
                        [33,5,5,1.7407489499999997],
                        [60,5,5,1.0558709999999998],
                        [80,5,5,0.7981709999999992],
                        [33,200,5,4.307377949999999],
                        [60,200,5,3.6224999999999996],
                        [80,200,5,3.364799999999999],
                        [33,2000,5,27.999337949999997],
                        [60,2000,5,27.314459999999997],
                        [80,2000,5,27.056759999999997],
                        [33,5,10,1.7078434499999997],
                        [60,5,10,1.0229654999999998],
                        [80,5,10,0.7652654999999993],
                        [33,200,10,2.99115795],
                        [60,200,10,2.3062799999999997],
                        [80,200,10,2.0485799999999994],
                        [33,2000,10,14.837137949999999],
                        [60,2000,10,14.152259999999998],
                        [80,2000,10,13.894559999999998],
                        [33,5,55,1.680920768181818],
                        [60,5,55,0.9960428181818181],
                        [80,5,55,0.7383428181818175],
                        [33,200,55,1.9142506772727268],
                        [60,200,55,1.229372727272727],
                        [80,200,55,0.9716727272727265],
                        [33,2000,55,4.068065222727272],
                        [60,2000,55,3.3831872727272723],
                        [80,2000,55,3.1254872727272716]]
    for case in inputs_answers:
        assert carbon_dioxide(case[0],case[1],case[2]) == case[3]