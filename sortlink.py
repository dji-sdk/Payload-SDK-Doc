#coding:UTF-8
#------文件操作------
import os

def __listFile__(path, isDeep=True):
    import glob
    _list = []
    if isDeep:
        try:
            for root, dirs, files in os.walk(path):
                for fl in files:
                    _list.append('%s\%s' % (root, fl))                
        except:
            pass
    else:
        for fn in glob.glob( path + os.sep + '*' ):
            if not os.path.isdir(fn):
                _list.append('%s' % path + os.sep + fn[fn.rfind('\\')+  1:])
    return _list
 
def listFile(remotePath, exclude=None, isDeep=True):
    _list = []
    _subdir = []
    _delList = []
    # 本地
    _list = __listFile__(remotePath, isDeep)
    if not _list:return _list
     
    if exclude and type(exclude)==list:
        for extFile in exclude:
            for fp in _list:
                if extFile.lower() == os.path.basename(fp).lower():
                    _delList.append(fp)
    if _delList:
        for delfp in _delList:
            _list.remove(delfp)
    return _list

def replaceHtmlStaticLink(fileList):
    for srcFile in fileList:
        if srcFile.endswith('.html') or srcFile.endswith('.css'):

            srcFile = srcFile.replace('\\', '/')
            count = srcFile.count('/') - 2
            prefix = count * '../'
            f = open(srcFile, 'r')
            data = f.read()
            f.close()
            print len(data)
            data = data.replace('"/stylesheets', '"' + prefix + 'stylesheets')
            data = data.replace('"/images', '"' + prefix + 'images')
            data = data.replace('"/fonts', '"' + prefix + 'fonts')
            data = data.replace('"/javascripts', '"' + prefix + 'javascripts')
            data = data.replace('"/images', '"' + prefix + 'images') 
            data = data.replace('"/assets', '"' + prefix + 'assets')
            temp = data.split('<div id="documentation-page"')
            if len(temp) == 2:
                header = temp[0]
                temp1 = temp[1].split('<footer id="site-footer"')
                content = '<div id="documentation-page"' + temp1[0]
                footer = ''
                if len(temp1) == 2:
                    footer = '<footer id="site-footer"' + temp1[1]
                content = content.replace('href="/', 'href="' + prefix)
                data = header + content + footer
            # data = data.replace('href="/', 'href="' + prefix)
            data = data.replace('\'//www.google', '\'http://www.google')
            print '====>', srcFile, len(data)
            data = '<script>window.pathPrefix="' + prefix + '";</script>' + data
            f = open(srcFile, 'w')
            f.write(data)
            f.close()

if __name__ == '__main__':
    fileList = listFile('./public')
    replaceHtmlStaticLink(fileList)

