cd ..
cd quiche/
/lib/linux-tools/5.15.0-73-generic/perf stat cargo run --bin quiche-server -- --cert apps/src/bin/cert.crt --key apps/src/bin/cert.key --root apps/src/bin
