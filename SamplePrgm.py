name = "Muthu"
sal = 10000
isMarried = True

print("My Name is ",name, type(name))
print("My Salary is ",sal, type(sal))
print("Im", isMarried, type(isMarried))

if(name == "Muthu"):
    print("Yes")
else:
    print("No")

if(name == "Muthu"):print("Name is Muthu")

browsers = ["Chrome","Firefox", "Edge", "IE 11"]
print(browsers[0:3])

browsers.append("Unknownbrowser")
print(browsers[0:5])

for browser in browsers: print(browser)

config = {
    "browser" : "Chrome",
    "site"  : "google",
    "type"  : "Smoke",
    "log"   : True
}

print(config.get("site"))

for conf in config.values(): print(conf)