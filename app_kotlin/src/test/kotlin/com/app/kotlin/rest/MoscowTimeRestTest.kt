package com.app.kotlin.rest

import com.app.kotlin.service.GetTimeService
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.extension.ExtendWith
import org.mockito.Mockito
import org.skyscreamer.jsonassert.JSONAssert
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest
import org.springframework.boot.test.mock.mockito.MockBean
import org.springframework.http.MediaType
import org.springframework.test.context.junit.jupiter.SpringExtension
import org.springframework.test.web.servlet.MockMvc
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders

@ExtendWith(SpringExtension::class)
@WebMvcTest(value = [MoscowTimeRest::class])
@MockBean(GetTimeService::class)
class MoscowTimeRestTest(
    @Autowired private val mockMvc: MockMvc,
    @Autowired private val getTimeServiceMock: GetTimeService
) {

    @Test
    fun getTimeInCorrectFormat() {
        val time = "2022-09-19T22:27:10.4370126+03:00"

        Mockito.`when`(
            getTimeServiceMock.getMoscowTime()
        ).thenReturn(time)

        val requestBuilder = MockMvcRequestBuilders.get("/moscow/time").accept(MediaType.APPLICATION_JSON)

        val result = mockMvc.perform(requestBuilder).andReturn()
        JSONAssert.assertEquals("{\"time\":\"${time}\"}", result.response.contentAsString, true)
    }
}
