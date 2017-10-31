DATADIR=$1

./../../../../../../fasttext/fasttext supervised -input "${DATADIR}/fast.train" -output "${DATADIR}/fast.model" -dim 50 -lr 0.01 -wordNgrams 4 -minCount 5 -bucket 200000 -epoch ${2} -thread 16 -loss softmax 

./../../../../../../fasttext/fasttext test "${DATADIR}/fast.model.bin" "${DATADIR}/fast.test"
./../../../../../../fasttext/fasttext test "${DATADIR}/fast.model.bin" "${DATADIR}/fast.train"

./../../../../../../fasttext/fasttext predict "${DATADIR}/fast.model.bin" "${DATADIR}/fast.test" > "${DATADIR}/fast.test.predict"

python tools/viewResult.py fast.test fast.test.predict
