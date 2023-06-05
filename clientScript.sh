cd ..
cd quiche/
/lib/linux-tools/5.15.0-73-generic/perf stat cargo run --bin quiche-client -- --no-verify https://10.0.0.2:4433/example.txt
