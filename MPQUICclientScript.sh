cd ..
cd quiche/
#cargo run --bin quiche-client -- --no-verify https://10.0.0.2:4433/example.txt
perf stat cargo run --bin quiche-client -- --no-verify https://10.0.4.1:4433/testVideo.mp4
