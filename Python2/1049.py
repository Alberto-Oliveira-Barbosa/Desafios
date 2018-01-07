# -*- coding: utf-8 -*-
p1 = raw_input()
p2 = raw_input()
p3 = raw_input()
animal = ""

if p1[0] == "v" and p2[0] == "a" and p3[0]=="c":
    animal = "aguia"

if p1[0] == "v" and p2[0] == "a" and p3[0]=="o":
    animal = "pomba"

if p1[0] == "v" and p2[0] == "m" and p3[0]=="o":
    animal = "homem"

if p1[0] == "v" and p2[0] == "m" and p3[0]=="h":
    animal = "vaca"

if p1[0] == "i" and p2[0] == "i" and p3 =="hematofago":
    animal = "pulga"

if p1[0] == "i" and p2[0] == "i" and p3 =="herbivoro":
    animal = "lagarta"

if p1[0] == "i" and p2[0] == "a" and p3[0] =="h":
    animal = "sanguessuga"

if p1[0] == "i" and p2[0] == "a" and p3[0] =="o":
    animal = "minhoca"

print animal
