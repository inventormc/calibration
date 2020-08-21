export DEVICE=0
export MODEL="roberta-base"  # options: bert-base-uncased, roberta-base
export TASK="SNLI"  # options: SNLI, MNLI, QQP, TwitterPPDB, SWAG, HellaSWAG
export LABEL_SMOOTHING=-1  # options: -1 (MLE), [0, 1]
export MAX_SEQ_LENGTH=256

if [ $MODEL = "bert-base-uncased" ]; then
    BATCH_SIZE=16
    LEARNING_RATE=2e-5
    WEIGHT_DECAY=0
fi

if [ $MODEL = "roberta-base" ]; then
    BATCH_SIZE=16
    LEARNING_RATE=1e-5
    WEIGHT_DECAY=0.1
fi

python3 train.py \
    --device $DEVICE \
    --model $MODEL \
    --task $TASK \
    --ckpt_path "ckpt/${TASK}_${MODEL}.pt" \
    --output_path "output/${TASK}_${MODEL}_OD.json" \
    --test_path "calibration_data/MNLI/test.txt" \
    --epochs 1 \
    --batch_size $BATCH_SIZE \
    --learning_rate $LEARNING_RATE \
    --weight_decay $WEIGHT_DECAY \
    --label_smoothing $LABEL_SMOOTHING \
    --max_seq_length $MAX_SEQ_LENGTH \
    --do_evaluate
