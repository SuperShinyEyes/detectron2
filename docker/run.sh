docker run --gpus all -it \
	--shm-size=8gb --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    -p 8002:8002 \
    -v /home/azureuser/.jupyter:/root/.jupyter \
    -v /home/azureuser/detectron2:/home/appuser/detectron2 \
	detectron2:v0 \
    jupyter lab --allow-root --ip='*' --port=8002 --no-browser --notebook-dir=/home/appuser/detectron2 

#  sudo docker run -it -p 8002:8002 -v /home/azureuser/.jupyter:/root/.jupyter -v /home/azureuser/notebooks/Mask_RCNN:/app waleedka/modern-deep-learning jupyter notebook --allow-root --ip='*' --port=8002 --no-browser --notebook-dir=/app