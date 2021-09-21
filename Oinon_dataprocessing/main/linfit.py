def linfit(list_X,list_Y,p0=None,xname=None,yname=None,title=None):#,xname,yname,title): #x数据，y数据，初始值p0，
    def f_l(x,k,b):
        return k*x+b
    k,b=curve_fit(f_l,list_X,list_Y,p0)[0] #拟合曲线斜率和截距
    r=stats.pearsonr(list_X,list_Y) [0]#皮尔逊相关系数
    plt.scatter(list_X,list_Y,color="black",marker="o",label="data")
    X_min=list_X[list_X.index(min(list_X))]
    X_max=list_X[list_X.index(max(list_X))]
    list_x=np.arange(X_min*0.9,X_max*1.1,0.01)
    list_y=k*list_x+b
    plt.plot(list_x,list_y,color="blue",label="fit:k=%7.5f,b=%7.5f,r=%7.5f"%(k,b,r))

    plt.title(title)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.legend()