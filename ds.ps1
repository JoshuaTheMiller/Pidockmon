# ds = dockerscript

cd "C:\Users\mille\Desktop\Pidockmon";

docker build -t pidockmon .;

# put in a note that I forgot to bind mount (-v) also include screenshot.

docker run --rm  -v /var/run/docker.sock:/var/run/docker.sock -p 5000:5000 -d --name pdm pidockmon;

