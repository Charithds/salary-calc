# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:33:54 2022

@author: Charith
"""
import streamlit as st

def calcTax(yearly):
    taxable = yearly - 1800000
    totalTax = 0
    taxRate = 4
    while taxable > 0:
        totalTax = totalTax + min(taxable, 1200000) * taxRate / 100
        taxRate = taxRate + 4
        taxable = taxable - 1200000
        if taxRate == 32:
            totalTax = totalTax + taxable * taxRate / 100
    return totalTax

def calcEPF(yearly):
    return yearly * 0.08
    

def calc(salaryDic):
    basic = salaryDic['basic'] 
    otherPAYE = salaryDic['otherPAYE']
    other = salaryDic["other"]
    
    totalSalary = basic + otherPAYE + other
    taxableYearly = (basic + otherPAYE) * 12
    epfableYearly = basic * 12
    
    totalTax = calcTax(taxableYearly)
    totalEPF = calcEPF(epfableYearly)
    
    st.text("Total tax per month: " + str(totalTax/12))
    st.text("Total EPF per month: " + str(totalEPF/12))
    st.text("Salary after tax: " + str(totalSalary - totalTax/12))
    st.text("Salary after tax and epf: " + str(totalSalary - totalEPF/12 - totalTax/12 ))

def main():
    st.title("Salary Calculator Sri Lanka")
    
    basic = st.number_input("Enter your basic salary")
    otherPAYE = st.number_input("Enter your other PAYE")
    other = st.number_input("Total other")
    
    salaryDic = {}
    salaryDic['basic'] = basic
    salaryDic['otherPAYE'] = otherPAYE
    salaryDic["other"] = other
    
    calc(salaryDic)

if __name__ == '__main__':
    main()
