


Style Transfer
https://github.com/lengstrom/fast-style-transfer

Checkpoint files
https://video.udacity-data.com/topher/2017/January/587d1865_rain-princess/rain-princess.ckpt
https://video.udacity-data.com/topher/2017/January/588aa800_la-muse/la-muse.ckpt
https://video.udacity-data.com/topher/2017/January/588aa846_udnie/udnie.ckpt
https://video.udacity-data.com/topher/2017/January/588aa883_scream/scream.ckpt
https://video.udacity-data.com/topher/2017/January/588aa89d_wave/wave.ckpt
https://video.udacity-data.com/topher/2017/January/588aa8b6_wreck/wreck.ckpt


## Dependencies

```CMD
conda create -n style-transfer python=3
conda activate style-transfer
conda install tensorflow scipy pillow
pip install moviepy
python -c "import imageio; imageio.plugins.ffmpeg.download()"
```

new env "style-transfer"


1. activate style-transfer
2. cd to directory
3. run python evaluation script
* checkpoint file (pre-trained ai)
* input image 
* output image

```CMD
activate style-transfer

cd .\github\UdacityDeepLearning_NanoDegree\1_neural_networks\fast-style-transfer-master

python evaluate.py --checkpoint ./rain-princess.ckpt --in-path ./examples/content/memoji.png --out-path ./output_image.jpg
```


python evaluate.py --checkpoint ./rain-princess.ckpt --in-path <path_to_input_file> --out-path ./output_image.jpg

python evaluate.py --checkpoint ./wave.ckpt --in-path ./examples/content/memoji.png  --out-path ./output_image0.jpg
python evaluate.py --checkpoint ./udnie.ckpt --in-path ./examples/content/memoji.png  --out-path ./output_image1.jpg
python evaluate.py --checkpoint ./la-muse.ckpt --in-path ./examples/content/memoji.png  --out-path ./output_image2.jpg
python evaluate.py --checkpoint ./scream.ckpt --in-path ./examples/content/memoji.png  --out-path ./output_image3.jpg
