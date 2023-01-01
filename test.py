import torch
import time
import cv2
import imageio
from network import TransformNetwork
from image_utils import imload, imsave, imloadFrame, imsaveframe

def load_transform_network(args):
    transform_network = TransformNetwork()
    transform_network.load_state_dict(torch.load(args.model_load_path))
    return transform_network

def network_test(args):
    device = torch.device("cuda" if args.cuda_device_no >= 0 else 'cpu')

    transform_network = load_transform_network(args)
    transform_network = transform_network.to(device)
    start = time.time()

    # image test
    if(args.test_content is not None):
        framecount = 1
        input_image = imload(args.test_content, args.imsize).to(device)
        with torch.no_grad():
            output_image = transform_network(input_image)
            imsave(output_image, args.output)

    # video test
    if(args.input_video is not None):
        input_video = cv2.VideoCapture(args.input_video)
        video = imageio.get_reader(args.input_video)
        fps = video.get_meta_data()['fps']
        print("fps = ", fps)

        # Check if video opened successfully
        if not input_video.isOpened():
            print("Error opening video stream or file")

        else:
            framecount = 0

            if args.output_video is not None:
                print("output video is not None")
                frame_width = int(input_video.get(3))
                frame_height = int(input_video.get(4))
                
                out = cv2.VideoWriter(args.output_video,cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))
        
            while input_video.isOpened():
                ret, frame = input_video.read()
                if ret:
                    framecount += 1
                    tensor = imloadFrame(frame).to(device)
                    with torch.no_grad():
                        tensor = transform_network(tensor)
                        if(args.output_video is not None):
                            output_frame = imsaveframe(tensor, out)
                        else:
                            output_frame = imsaveframe(tensor)
                        cv2.imshow('Press Q to exit', output_frame)
                        if cv2.waitKey(25) & 0xFF == ord('q'):
                            break
                else:
                    break
            input_video.release()
            if args.output_video is not None:
                out.release()
            cv2.destroyAllWindows()
    
    stop = time.time()
    print(f"transfer time: {(stop - start)}s")

    return None
