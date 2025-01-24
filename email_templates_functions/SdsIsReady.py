def sds_is_ready_email(month, year,sds_link1,sds_link2,
                        send_feedback_link):
    return f""" <!doctype html>
<html>
  <body>
    <div
      style='background-color:#F5F5F5;color:#262626;font-family:"Helvetica Neue", "Arial Nova", "Nimbus Sans", Arial, sans-serif;font-size:16px;font-weight:400;letter-spacing:0.15008px;line-height:1.5;margin:0;padding:32px 0;min-height:100%;width:100%'
    >
      <table
        align="center"
        width="100%"
        style="margin:0 auto;max-width:600px;background-color:#FAFAFA;border-radius:48px"
        role="presentation"
        cellspacing="0"
        cellpadding="0"
        border="0"
      >
        <tbody>
          <tr style="width:100%">
            <td>
              <div style="padding:16px 24px 16px 24px;background-color:#e8f0f0">
                <img
                  alt="Sample product"
                  src="https://pouch.jumpshare.com/preview/j2OHpNjxoY5cdnK42kh04okk4lYhialWELU9Voc4AidUnWVTzrAkLws0wcZ-7OGc2cWq9vuQLLMgczup72392EAFtBShOikdRJ0JuyX-yJ4"
                  style="outline:none;border:none;text-decoration:none;vertical-align:top;display:inline-block;max-width:100%"
                />
              </div>
              <div style="background-color:#e8f0f0;padding:0px 56px 32px 40px">
                <div
                  style="background-color:#FFFFFF;border-radius:12px;padding:16px 24px 24px 24px"
                >
                  <div
                    style='color:#2563EB;font-size:18px;font-family:Charter, "Bitstream Charter", "Sitka Text", Cambria, serif;font-weight:bold;padding:12px 24px 0px 24px'
                  >
                    Your SDS is Ready
                  </div>
                  <div
                    style="font-size:13px;font-weight:normal;padding:16px 24px 16px 24px"
                  >
                    Find attached your SDS report for {month} {year}. Kindly review
                    the document and reply to this email with your feedback
                    using the attached template
                  </div>
                  <div style="padding:16px 24px 16px 24px">
                    <div
                      style="background-color:#F5F5F5;padding:16px 0px 16px 16px"
                    >
                      <table
                        align="center"
                        width="100%"
                        cellpadding="0"
                        border="0"
                        style="table-layout:fixed;border-collapse:collapse"
                      >
                        <tbody style="width:100%">
                          <tr style="width:100%">
                            <td
                              style="box-sizing:content-box;vertical-align:middle;padding-left:0;padding-right:0;width:50px"
                            >
                              <div style="padding:4px 8px 16px 12px">
                                <img
                                  alt=""
                                  src="https://ui-avatars.com/api/?size=128"
                                  height="32"
                                  width="32"
                                  style="outline:none;border:none;text-decoration:none;object-fit:cover;height:32px;width:32px;max-width:100%;display:inline-block;vertical-align:middle;text-align:center;border-radius:4px"
                                />
                              </div>
                            </td>
                            <td
                              style="box-sizing:content-box;vertical-align:middle;padding-left:0;padding-right:0;width:180px"
                            >
                              <div
                                style="font-size:12px;font-weight:normal;text-align:center;padding:12px 12px 16px 12px"
                              >
                                ENI_SDS_FEEDBACK_template
                              </div>
                            </td>
                            <td
                              style="box-sizing:content-box;vertical-align:middle;padding-left:0;padding-right:0"
                            >
                              <div
                                style="text-align:center;padding:12px 16px 16px 12px"
                              >
                                <a
                                  href="{sds_link1}"
                                  style="color:#000000;font-size:11px;font-weight:bold;background-color:#FFFFFF;border-radius:4px;display:inline-block;padding:8px 12px;text-decoration:none"
                                  target="_blank"
                                  ><span
                                    ><!--[if mso
                                      ]><i
                                        style="letter-spacing: 12px;mso-font-width:-100%;mso-text-raise:18"
                                        hidden
                                        >&nbsp;</i
                                      ><!
                                    [endif]--></span
                                  ><span>Download</span
                                  ><span
                                    ><!--[if mso
                                      ]><i
                                        style="letter-spacing: 12px;mso-font-width:-100%"
                                        hidden
                                        >&nbsp;</i
                                      ><!
                                    [endif]--></span
                                  ></a
                                >
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <div style="height:16px"></div>
                    <div
                      style="background-color:#F5F5F5;padding:16px 0px 16px 16px"
                    >
                      <table
                        align="center"
                        width="100%"
                        cellpadding="0"
                        border="0"
                        style="table-layout:fixed;border-collapse:collapse"
                      >
                        <tbody style="width:100%">
                          <tr style="width:100%">
                            <td
                              style="box-sizing:content-box;vertical-align:middle;padding-left:0;padding-right:0;width:50px"
                            >
                              <div
                                style="text-align:center;padding:4px 8px 16px 12px"
                              >
                                <img
                                  alt=""
                                  src="https://ui-avatars.com/api/?size=128"
                                  height="32"
                                  width="32"
                                  style="outline:none;border:none;text-decoration:none;object-fit:cover;height:32px;width:32px;max-width:100%;display:inline-block;vertical-align:middle;text-align:center;border-radius:4px"
                                />
                              </div>
                            </td>
                            <td
                              style="box-sizing:content-box;vertical-align:middle;padding-left:0;padding-right:0;width:180px"
                            >
                              <div
                                style="font-size:12px;font-weight:normal;text-align:center;padding:12px 12px 16px 12px"
                              >
                                ENI_SDS_FEEDBACK_template
                              </div>
                            </td>
                            <td
                              style="box-sizing:content-box;vertical-align:middle;padding-left:0;padding-right:0"
                            >
                              <div
                                style="text-align:center;padding:8px 12px 8px 12px"
                              >
                                <a
                                  href="{sds_link2}"
                                  style="color:#0A0A0A;font-size:11px;font-weight:bold;background-color:#FFFFFF;border-radius:4px;display:inline-block;padding:8px 12px;text-decoration:none"
                                  target="_blank"
                                  ><span
                                    ><!--[if mso
                                      ]><i
                                        style="letter-spacing: 12px;mso-font-width:-100%;mso-text-raise:18"
                                        hidden
                                        >&nbsp;</i
                                      ><!
                                    [endif]--></span
                                  ><span>Download</span
                                  ><span
                                    ><!--[if mso
                                      ]><i
                                        style="letter-spacing: 12px;mso-font-width:-100%"
                                        hidden
                                        >&nbsp;</i
                                      ><!
                                    [endif]--></span
                                  ></a
                                >
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                  <div
                    style='color:#1348bc;font-size:14px;font-family:Bahnschrift, "DIN Alternate", "Franklin Gothic Medium", "Nimbus Sans Narrow", sans-serif-condensed, sans-serif;font-weight:bold;padding:16px 24px 4px 24px'
                  >
                    READY WITH YOUR FEEDBACK
                  </div>
                  <div
                    style="font-size:12px;font-weight:normal;padding:4px 24px 16px 24px"
                  >
                    Reply to this email will your feedback. Use he button below
                    to reply
                  </div>
                  <div style="text-align:center;padding:28px 24px 16px 24px">
                    <a
                      href="{send_feedback_link}"
                      style="color:#FFFFFF;font-size:11px;font-weight:bold;background-color:#477606;border-radius:4px;display:inline-block;padding:12px 20px;text-decoration:none"
                      target="_blank"
                      ><span
                        ><!--[if mso
                          ]><i
                            style="letter-spacing: 20px;mso-font-width:-100%;mso-text-raise:30"
                            hidden
                            >&nbsp;</i
                          ><!
                        [endif]--></span
                      ><span>Send Feedback</span
                      ><span
                        ><!--[if mso
                          ]><i
                            style="letter-spacing: 20px;mso-font-width:-100%"
                            hidden
                            >&nbsp;</i
                          ><!
                        [endif]--></span
                      ></a
                    >
                  </div>
                </div>
                <div
                  style="font-size:12px;font-weight:normal;text-align:center;padding:16px 72px 16px 68px"
                >
                  You have received this notification because you are a user of
                  the NLNG IVCO App
                </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
</html>
"""