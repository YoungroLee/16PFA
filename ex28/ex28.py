# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/book/ex28.html

print(" 1. True and True + %s" % str(True and True))
print(" 2. False and True = %s" %str(False and True))
print(" 3. 1==1 and 2==1 = %s" %str((1==1) and  (2==1)))
print(" 4. 'test' == 'test' = %s" % str('test' == 'test'))
print(" 5. 1==1 or 2!=1 = %s" % ((1 ==1) or (2 != 1)))
print(" 6. True and 1==1 =%s" %str(True and (1 ==1)))
print(" 7. False and 0!=0 = %s" % str(False and (0 !=0)))
print(" 8. True or 1==1 = %s" % True or (1 == 1))
print(" 9. 'test' == 'testing' = %s" %str('test' == 'testing'))
print("10. 1!=0 and 2==1 = %s" % str(1 !=0) and (2 == 1))
print("11. 'test' !='testing' = %s" % str('test' != 'testing'))
print("12. 'test'==1 = %s" % str('test'== 1))
print("13. not(True and False) = %s" % (not (True and False)))
print("14. not(1==1 and 0!=1) = %s" % (not ((1 ==1) and (0 !=1))))
print("15. not(10==1 or 1000=1000) = %s" %(not (not ((10 == 1) or (1000 == 1000))))