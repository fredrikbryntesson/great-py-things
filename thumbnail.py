import subprocess, sys, shutil, random, string
input = sys.argv[1]
input = input.split('=')[1]
input = 'https://img.youtube.com/vi/' + input + '/maxresdefault.jpg'
subprocess.check_call(['wget', input])


newName = ''.join(random.choice(string.lowercase) for i in range(10))
shutil.move('maxresdefault.jpg', newName + '.jpg')



