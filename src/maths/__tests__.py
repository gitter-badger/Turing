# -*- coding: utf-8 -*-

from tests.framework import expect

from maths.parser import Parser
from maths.evaluator import Evaluator

tests = [
    # basic parsing
    ("42", 42, "42"),
    ("-42", -42, "-42"),

    # basic operators
    ("2+2", 4, "2 + 2"),
    ("3*3", 9, "3 * 3"),
    ("142        -9   ", 133, "142 - 9"),
    (" 50/10", 5, "50 / 10"),
    ("72+  15", 87, "72 + 15"),
    (" 12*  4", 48, "12 * 4"),
    ("4*2.5 + 8.5+1.5 / 3.0", 19, "4 * 2.5 + 8.5 + 1.5 / 3"),
    (" 2-7", -5, "2 - 7"),
    ("2 -4 +6 -1 -1- 0 +8", 10, "2 - 4 + 6 - 1 - 1 - 0 + 8"),
    (" 2*3 - 4*5 + 6/3 ", -12, "2 * 3 - 4 * 5 + 6 / 3"),
    ("10/4", 2.5, "10 / 4"),

    # unary edge cases
    ("--5", 5, "--5"),
    ("0--5", 5, "0 - -5"),

    # basic functions
    ("ceil(pi)", 4, "ceil(pi)"),
    ("floor(e)", 2, "floor(e)"),
    ("sqrt(49)", 7, "sqrt(49)"),
    ("sqrt(2)^2", 2, "sqrt(2) ^ 2"),
    ("cos(0)", 1, "cos(0)"),
    ("sin(pi)", 0, "sin(pi)"),
    ("deg(2pi)", 360, "deg(2 * pi)"),
    ("round(asin(acos(atan(tan(cos(sin(0.5)))))),5)", 0.5, "round(asin(acos(atan(tan(cos(sin(0.5)))))), 5)"),

    ("binomial(3,2)", 3, "binomial(3, 2)"),
    ("binomial(3 , 0)", 1, "binomial(3, 0)"),

    ("average(12,82,74,36,14,94)", 52, "average(12, 82, 74, 36, 14, 94)"),
    ("sum(1,8,9,6,24,54,354)", 456, "sum(1, 8, 9, 6, 24, 54, 354)"),
    ("[8,5,42,96,31,84,35] [-4]", 96, "[8, 5, 42, 96, 31, 84, 35][-4]"),
    ("[1,2,3,4][2]", 3, "[1, 2, 3, 4][2]"),
    ("[42,{x,y,z}(x*abs({x, y}(x - y)(y, z))),38][1](4,3,5)", 8,
     "[42, {x, y, z}(x * abs({x, y}(x - y)(y, z))), 38][1](4, 3, 5)"),

    ("(2+2)==4", True, "(2 + 2) == 4"),
    ("vrai xor true", False, "VRAI XOR VRAI"),
    ("\"abc\"+\"def\"", "abcdef", "\"abc\" + \"def\""),

    # list operators
    ("[1,2,3]+[3,4,5]", [1, 2, 3, 3, 4, 5], "[1, 2, 3] + [3, 4, 5]"),
    ("[1,2,3]-[3,4,5]", [1, 2], "[1, 2, 3] - [3, 4, 5]"),
    ("-[1,2,3]", [3, 2, 1], "-[1, 2, 3]"),
    ("3*[1,2,3]", [1, 2, 3, 1, 2, 3, 1, 2, 3], "3 * [1, 2, 3]"),
    ("[1,2,3]&[2,3,4]", [2, 3], "[1, 2, 3] & [2, 3, 4]"),
    ("[1,2,3]|[2,3,4]", [1, 2, 3, 4], "[1, 2, 3] | [2, 3, 4]"),
    ("[1,2,3]xor[3,4,5]", [1, 2, 4, 5], "[1, 2, 3] XOR [3, 4, 5]"),

    # complex lambda tests
    ("map({a}({a,b}(b*a)(2,a)),[1,2,3,4,5,6])", [2, 4, 6, 8, 10, 12],
     "map({a}({a, b}(b * a)(2, a)), [1, 2, 3, 4, 5, 6])"),
    ("-filter({a}(a<0),[-2,-1,0,1,2])", [-1, -2], "-filter({a}(a < 0), [-2, -1, 0, 1, 2])"),

    # leo
    ("gcd(248,4584)", 8, "gcd(248, 4584)"),
    ("lcm(904,1356)", 2712, "lcm(904, 1356)"),

    ("slice([1,2,3,4,5,6,7,8],2,6)", [3, 4, 5, 6], "slice([1, 2, 3, 4, 5, 6, 7, 8], 2, 6)"),

    ("round(variance([2.75,1.75,1.25,0.25,0.5,1.25,3.5]),2)", 1.18,
     "round(variance([2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]), 2)"),
    ("round(variance_sample([2.75,1.75,1.25,0.25,0.5,1.25,3.5]),2)", 1.37,
     "round(variance_sample([2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]), 2)"),
    ("harmonic_mean(2.5,3,10)", 3.6, "harmonic_mean(2.5, 3, 10)"),

    ("5e+99/2e45", 2.5e54, "5e99 / 2e45"),
    ("5e-99/2e-45", 2.5e-54, "5e-99 / 2e-45")
]


def run_tests():
    ev = Evaluator()

    for e, res, beaut in tests:
        ret = ev.evaluate(e)
        expect(ret, res)
        expect(ev.beautified, beaut)
