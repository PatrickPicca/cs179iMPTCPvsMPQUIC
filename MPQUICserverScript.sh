cd ..
cd quiche/
#cargo run --bin quiche-server -- --cert apps/src/bin/cert.crt --key apps/src/bin/cert.key --root apps/src/bin --listen 10.0.0.2:4433
perf stat cargo run --bin quiche-server -- --cert apps/src/bin/cert.crt --key apps/src/bin/cert.key --root apps/src/bin --listen 10.0.4.1:4433
