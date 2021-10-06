from dirsync import sync

sourcedir = r"C:\Users\data121\Dropbox\דרך הנדסה\Acad setting"
targetdir = r"C:\Acad setting"

sync(sourcedir, targetdir, "sync" , twoway = True)
sync(targetdir, sourcedir, "sync")