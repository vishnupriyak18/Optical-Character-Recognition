def clean_result(result):
    det_text = []
    for x in range(len(result)):
        det_text.append(str(result[x][1]))
    len_list = [i for i in range(len(det_text))]
    det_text = dict(zip(len_list,det_text))
    return det_text
    
def ocr_detect(image):
    
    import easyocr
    import cv2
    import matplotlib as mlp

    import matplotlib.pyplot as plt
    rcp = mlp.rcParams
    rcp['figure.figsize'] = 8, 16
    reader = easyocr.Reader(['en']) # need to run only once to load model into memory
    result = reader.readtext(image)
    image = cv2.imread(image)
    cord = []
    for i in range(len(result)):
        cord.append(result[i][0])
    for c in cord:
        x_min, y_min = [int(min(idx)) for idx in zip(*c)]
        x_max, y_max = [int(max(idx)) for idx in zip(*c)]
        cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(0,0,255),2)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    
    plt.savefig('marked_files/image.png')
    text_clean = clean_result(result)
    return text_clean
    