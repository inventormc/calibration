export TEST_PATH="output/SNLI_roberta-base_OD.json"
# export TRAIN_PATH="output/dev/QQP_QQP_roberta-base.json"

python3 calibrate.py \
    --test_path $TEST_PATH \
    --do_evaluate
