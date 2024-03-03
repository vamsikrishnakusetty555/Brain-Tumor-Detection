import streamlit as st
import Home

st.title(":orange[Brain Tumor] Detection Portal")
st.markdown('''
<style>
.text{
text-align:justify;
}
</style>
''', unsafe_allow_html=True)
Home.sidebar()
st.header("Project Overview")
st.markdown(
    "<div class='text'>The anomalous development of cells in brain causes brain tumor that may lead to death. The rate of deaths can be reduced by early detection of tumor. Most common method to detect the tumor in brain is the use of Magnetic Resonance Imaging (MRI). MR images are considered because it gives a clear structure of the tumor."
    "The aim of our project is to develop an efficient method to detect the brain tumor.</div>", unsafe_allow_html=True)
features = st.container()
with features:
    st.header("Features")
    f1, f2 = st.columns([1.5, 3])
    with f1:
        st.metric(label="✅Detection of", value="Brain Tumor")
    with f2:
        st.metric(label="✅Highlights", value="Tumor Location")
    f3, f4 = st.columns([1.5, 3])
    with f3:
        st.metric(label="✅Voice", value="Result")
    with f4:
        st.metric(label="✅Focusses on", value="Early-stage Detection")
    f5, f6 = st.columns([1.5, 3])
    with f6:
        st.metric(label="✅Trained with", value="Large Datasets", delta="4600 Images")
    with f5:
        st.metric(label="✅High", value="Accuracy", delta="95%")

dataset = st.container()
with dataset:
    st.header("Dataset")
    st.markdown(
        "<div  class='text'>The dataset utilized in this project comprises approximately 4600 images sourced from repositories hosted by the University of California, Irvine (UCI) and Kaggle. The images span diverse categories and contexts, curated to facilitate the development and evaluation of machine learning models, computer vision algorithms, and related research endeavors.</div>",
        unsafe_allow_html=True)
    dataset_url = "https://drive.google.com/uc?id=1wKu-SlTEh93cDGy0MiBGwxWuchi7015o&export=download"
    st.markdown(f"##### **🔗Download the dataset [here]({dataset_url}).**")
    st.caption(":orange[**Know More !!**]")
    q = """⏩Origin and Sources/⏩Acknowledgments"""
    a = """The dataset amalgamates images sourced from the renowned academic institution, **the University of California, Irvine (UCI)**, renowned for its comprehensive repositories of machine learning datasets. Additionally, images were sourced from **Kaggle**, a prominent platform hosting datasets and fostering collaborative data science projects. The collaborative effort ensures a rich and varied collection suitable for addressing a spectrum of research questions and applications./
    The construction and dissemination of this dataset owe gratitude to the academic community, data contributors, and platforms such as **UCI** and **Kaggle**. Their collective efforts and contributions have enriched the data landscape, fostering innovation, collaboration, and advancements in machine learning and computer vision research."""
    for i, j in zip(q.split("/"), a.split("/")):
        with st.expander(i):
            st.write(f"<p class='text'>{j}</p>", unsafe_allow_html=True)
ML_Model = st.container()
with ML_Model:
    st.header("Our Model")
    st.markdown(
        "<div class='text'>Our project employs Convolutional Neural Networks (CNN) and the MobileNet classifier to train a model for brain tumor detection. With a dataset sourced from reputable repositories like the University of California, Irvine (UCI) and Kaggle, our model achieves an impressive **95% accuracy** rate. This achievement underscores the efficacy of our approach in accurately identifying brain tumors from Magnetic Resonance Imaging (MRI) scans. Our project represents a significant advancement in leveraging deep learning and medical imaging to enhance early tumor detection, potentially saving lives and improving healthcare outcomes.</div>",
        unsafe_allow_html=True)
    dataset_url = "https://drive.google.com/drive/folders/1SgDykLtVIYcwyh4HKC4EA0A_7QB3vfn-?usp=sharing"
    st.markdown(f"##### **🔗Download Our Model [here]({dataset_url}).**")
    st.caption(":orange[**Know More !!**]")
    with st.expander("⏩MobileNet Classifier"):
        c1, c2 = st.columns([3, 3])
        with c1:
            paragraph = """
                <div style="text-align: justify">
                <ul>
                    <li>The highest possibility accuracy occurrence in image classification is MobileNet and then AlexNet.</li>
                    <li>A depthwise separable convolution is made from two operations:
                        <ul>
                            <li>Depthwise convolution</li>
                            <li>Pointwise convolution</li>
                        </ul>
                    </li>
                    <li>Depthwise separable convolution is a depthwise convolution followed by a pointwise convolution.</li>
                </ul>
                </div>
                """
            st.markdown(paragraph, unsafe_allow_html=True)
        with c2:
            st.image("btd/model/mobilenet.png")
    with st.expander("⏩Depthwise Convolution"):
        paragraph = '''
        <div style="text-align: justify">

        - **Depthwise Convolution**: Depthwise Convolution is a type of convolution where we apply a single convolutional filter for each input channel.

        - **Regular 2D Convolution**: In the regular 2D convolution performed over multiple input channels, all input channels are convolved with the same filter.

        - **Depthwise Convolution vs Regular 2D Convolution**: In contrast, depthwise convolutions keep each channel separate, enabling independent feature extraction across channels.

        </div>

        '''
        st.markdown(paragraph, unsafe_allow_html=True)
    with st.expander("⏩Pointwise Convolution"):
        paragraph = '''
        <div style="text-align: justify;">
        <strong>Pointwise Convolution</strong> is a type of convolution that uses a 1x1 kernel (a kernel that iterates through every single point).
        It can be used in conjunction with depthwise convolutions to produce an efficient class of convolutions.
        </div>
        '''
        st.markdown(paragraph, unsafe_allow_html=True)
