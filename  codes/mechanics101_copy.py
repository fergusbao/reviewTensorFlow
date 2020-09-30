# import modules
import argparse
import sys
import tensorflow as tf

def main(_):
    print(parser)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--learning_rate',type=float,default=1e-4,help='Initial learning rate for AdamOptimizer.')
    parser.add_argument('--max_steps',type=int,default=20000,help='Number of steps to run trainer.')
    parser.add_argument('--batch_size',type=int,default=50,help='Batch size.')
    parser.add_argument('--input_data_dir',type=str,default='/home/h/Documents/models/tutorials/image/mnist/data',help='input data directory')
    parser.add_argument('--log_dir',type=str,default='./tf_mechanics_101_logs',help='directory to put log data')
    parser.add_argument('--fake_data',default=False,help='If true, uses fake data for unit testing.',action='store_true')
    FLAGS, unparsed = parser.parse_known_args()
    tf.compat.v1.app.run(main=main,argv=[sys.argv[0]]+unparsed)