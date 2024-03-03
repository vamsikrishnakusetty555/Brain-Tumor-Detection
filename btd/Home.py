import streamlit as st
import base64

def css():
    st.markdown("""
    <style>
    .intro{
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

def expanders():
    q = """◼ How long a brain tumor patient can live?/◼ What is the last stage of brain tumor?/◼ Can brain tumor be cured?/◼ Are brain tumors genetic?
    /◼ Do you sleep a lot with a brain tumor?/◼ Does brain tumor cause hair loss?/◼ Can a brain tumor develop in 6 months?/◼ What is the physical test for brain tumor?
    /◼ How to diagnose brain tumor?/◼ At what age brain tumor can occur?/◼ What is the simple test for brain tumor?/◼ How can I test for brain tumor at home?"""
    a = """The 5-year relative survival rate for people younger than age 15 is about 75%. For people age 15 to 39, the 5-year relative survival rate nears 72%. The 5-year relative survival rate for people age 40 and older is 21%. Experts measure relative survival rate statistics for a brain tumor every 5 years./
    The patient will be especially sleepy, as drowsiness is the most common symptom of end-stage brain cancer and will likely have trouble swallowing, so eating and drinking may be difficult./
    The tumor can't always be removed completely. When it's possible, the surgeon works to remove as much of the brain tumor as can be done safely.
    /A small proportion of brain tumours are related to known genetic conditions. People who have one of these rare syndromes have an increased risk of getting a brain tumour./
    Poor sleep can be particularly bothersome, especially when patients with brain tumors also report hypersomnia. Hypersomnia was reported in more than 90% of primary brain-tumor patients undergoing cranial radiation therapy./
    Radiotherapy to the brain can cause hair loss or thinning. If you are having treatment to a particular part of the head, your hair usually falls out in that area. You might also have some hair loss on the opposite side of the head, where the radiotherapy beams pass through./
    The more aggressive a tumor is, the faster it grows. Generally speaking, a brain tumor can take several months or even years to develop./
    An MRI is considered the best way to look for tumours in the brain and spinal cord. Other special types of MRIs might be done including the following. MRA (magnetic resonance angiography) shows the structure of blood vessels in the brain and is useful in planning surgery./
    The diagnosis involves a physical exam, neurological exam, imaging of the brain or spine (depending on the patient's symptoms), and a specific biopsy based on the location of the tumor. The diagnosis is made either by a brain biopsy or by evaluating the spinal fluid, if the spinal fluid is thought to be involved.
    /Brain tumors can occur at any age. Brain tumors that occur in infants and children are very different from adult brain tumors, both in terms of the type of cells and the responsiveness to treatment./
    PET scan – you will be injected with a small amount of radioactive solution, which helps cancer cells show up brighter on the scan. Lumbar puncture – also called a spinal tap, a lumbar puncture uses a needle to collect a sample of cerebrospinal fluid from the spinal column, which is then checked for cancer cells./
    It's not possible to diagnose yourself with a brain tumor, even if you have concerning symptoms. Many symptoms of a brain tumor can be caused by other health conditions. The only way to know if you have a brain tumor is to get a medical diagnosis from a healthcare professional."""
    for i, j in zip(q.split("/"), a.split("/")):
        with st.expander(i):
            st.write(f"<p class='intro'>{j}</p>", unsafe_allow_html=True)

def app():
    css()
    st.title(":orange[Brain Tumor] Detection Portal")
    c1, c2 = st.columns([2.5, 2], gap="small")

    with c1:
        st.markdown("## Overview")
        st.markdown(
            "<p class='intro'>The Brain Tumor Detection Portal revolutionizes early diagnosis through MRI analysis. Leveraging advanced algorithms, our platform swiftly detects brain abnormalities with precision using MRI scan images as input. Journey with us as we embark on the creation of a user-friendly web application tailored to medical professionals.</p>",
            unsafe_allow_html=True)

    with c2:
        file_ = open("btd/images/brain2.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif" height="300" width="300">',
            unsafe_allow_html=True,
        )
    st.caption(":orange[**People Ask About ‼**]")
    expanders()
def sidebar():
    with st.sidebar:
        st.write("#")
        st.write("#")
        st.write("#")
        st.write("#")
        st.write("#")
        st.write("#")
        st.write("#")
        st.write("#")
        st.write("#")
        st.write("#")
        st.write("#")
        st.write("#")
        st.write("Contact: BrainScanInsights@gmail.com")
if __name__ == "__main__":
    sidebar()
    app()