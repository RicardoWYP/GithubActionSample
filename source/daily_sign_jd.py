import os
import requests

cookie = os.environ.get("JD_COOKIE")
# cookie = "__jdu=1305510986; shshshfpa=e50af6b1-000d-03ef-0a90-3702ded8ef5d-1606536915; pinId=gyJ25Ptd8XXb3ENE9zG3eA; jcap_dvzw_fp=5gscc84HtMXPp_R-nZPW9PRaHQU35qEvraOodw_JTYQXDmzoKpzYfeQav7ksbXSKkqQJww==; shshshfpx=e50af6b1-000d-03ef-0a90-3702ded8ef5d-1606536915; shshshfp=e16b9da67f3b3d8880499393962bb8da; mba_muid=1305510986; b_dw=1792; b_dh=937; b_dpr=2; b_webp=1; b_avif=1; whwswswws=; qid_uid=23a781ab-8672-448c-8ab0-10e43318d3cc; qid_fs=1701002225351; qid_ls=1701002225351; qid_ts=1701002225359; qid_vis=1; pin=%E9%9B%A8%E4%B8%8A%E6%99%A8%E6%98%9F; unick=%E9%9B%A8%E4%B8%8A%E6%99%A8%E6%98%9F; _tp=NKdUJ7sm5hNma5g1EcWjvCYeowp1uNMsu4kqRy%2BAt3CVYzhbfWwEo6zELDnwFN4r; _pst=%E9%9B%A8%E4%B8%8A%E6%99%A8%E6%98%9F; xxoo-tmp=zhHans; 3AB9D23F7A4B3C9B=5QC6PYI73TWCAOGD4ZOBHZ6UBCZDBUAPO6RYA7EGNVIZ2VUMYFJUI4A26MUYDSASN3LQZN2QJNNXIZN5WBBYZDKRO4; TrackID=1ptJm_GXM72aEi2kbXbAZ3XPGbZJMakrA5pK7lZnkIYIhP8SWpm4NC8V0YaoinNaqijORmoz-Uc70hQMyhPl4ICb8EdSrPOdDVFCxeDGLFCcJh5KNoKbH91AryW9tWhou; wxa_level=1; retina=1; cid=9; jxsid=17084852776292351662; appCode=ms0ca95114; webp=1; __jda=76161171.1305510986.1606536901.1706234270.1708485277.146; __jdv=76161171%7Cwww.google.com%7C-%7Creferral%7C-%7C1708485277649; __jdc=76161171; visitkey=4764267913474121067; wqmnx1=MDEyNjM4M3BkNDEwbE1oIFg3VzNIaykvLmkxc2Y0MkVIJlI%3D; cd_eid=jdd035QC6PYI73TWCAOGD4ZOBHZ6UBCZDBUAPO6RYA7EGNVIZ2VUMYFJUI4A26MUYDSASN3LQZN2QJNNXIZN5WBBYZDKRO4AAAAMNIN6NE6AAAAAADQEC6FLUWXIMSUX; sc_width=1792; PPRD_P=UUID.1305510986; jxsid_s_u=https%3A//home.m.jd.com/myJd/home.action; equipmentId=5QC6PYI73TWCAOGD4ZOBHZ6UBCZDBUAPO6RYA7EGNVIZ2VUMYFJUI4A26MUYDSASN3LQZN2QJNNXIZN5WBBYZDKRO4; fingerprint=3d3808ed7ab7f2ae9b3ce0866fda99f7; deviceVersion=122.0.0.0; deviceOS=; deviceOSVersion=; deviceName=Chrome; TrackerID=Yrrcy_BHzW6chZHZTDM2ZcKCHHy6DjhSv0x3RyYls1IAmEtHxznBQY3Abn8TQhUX5mlW4p1wte9L3F5dZmx4TKxlYNIt3AafAEdkip4JTqyRQ1pLSBfrdL6Vpgl_1lAg; pt_key=AAJl1WrdADCK7ggid2er8mUbPFu84IDQcNWIJMR8ziIIbH9j6WE7H2mh9RczI7V0z6xI8g_xBgE; pt_pin=%E9%9B%A8%E4%B8%8A%E6%99%A8%E6%98%9F; pt_token=bauv3nn9; pwdt_id=%E9%9B%A8%E4%B8%8A%E6%99%A8%E6%98%9F; sfstoken=tk01mb03e1c35a8sMiszeDIrMUI2gJnVcTbram/lFU85F471FHn1pXfnV0RcfE11kwbVNtiLcZ1NjeimnI+kvK+aqI9t; 3AB9D23F7A4B3CSS=jdd035QC6PYI73TWCAOGD4ZOBHZ6UBCZDBUAPO6RYA7EGNVIZ2VUMYFJUI4A26MUYDSASN3LQZN2QJNNXIZN5WBBYZDKRO4AAAAMNZGXNX4IAAAAACBEZAQGFQCYTZUX; __jdb=76161171.9.1305510986|146.1708485277; mba_sid=17084852776968781442372499109.9; __wga=1708485697296.1708485296962.1708485296962.1708485296962.3.1; jxsid_s_t=1708485697321; shshshfpb=BApXe2XemyuhA_Fih8krtW7hZXnVlHl6HB0QSbjpx9xJ1PlWgtQIOeJwSRK0CzK8qubA4; __jd_ref_cls=MMyJD_Main_Icon"

url = ("https://api.m.jd.com/client.action?functionId=signBeanAct&body=%7B%22fp%22%3A%22-1%22%2C%22shshshfp%22%3A%22-1"
       "%22%2C%22shshshfpa%22%3A%22-1%22%2C%22referUrl%22%3A%22-1%22%2C%22userAgent%22%3A%22-1%22%2C%22jda%22%3A%22-1"
       "%22%2C%22rnVersion%22%3A%223.9%22%7D&appid=ld&client=apple&clientVersion=10.0.4&networkType=wifi&osVersion=14"
       ".8.1&uuid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&openudid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&jsonp"
       "=jsonp_1645885800574_58482")

headers = {"Connection": 'keep-alive',
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Cache-Control": 'no-cache',
           "User-Agent": "okhttp/3.12.1;jdmall;android;version/10.3.4;build/92451;",
           "accept": "*/*",
           "connection": "Keep-Alive",
           "Accept-Encoding": "gzip,deflate",
           "Cookie": cookie
           }

response = requests.post(url=url, headers=headers)
print(response.text)
