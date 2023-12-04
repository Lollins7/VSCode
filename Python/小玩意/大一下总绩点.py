def socre(sf,gd,gll,jjx,yy,my,jsj,xl,ty,xz):
    return (sf*6+gd*4+gll*3+jjx*3+yy*4+my*3+jsj*3+xl*1+ty*1+xz*0.35)/28.35

sf = eval(input("数分"))
gd = eval(input("高代"))
gll = eval(input("概率论"))
jjx = eval(input("经济学"))
yy = eval(input("英语"))
my = eval(input("马原"))
jsj = eval(input("计算机"))
xl = eval(input("心理"))
ty = eval(input("体育"))
xz = eval(input("形政"))

print(socre(sf,gd,gll,jjx,yy,my,jsj,xl,ty,xz))